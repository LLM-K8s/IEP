from typing import List

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Request

from application.auth_service import get_current_user
from application.course_DTO import GetCourseDTO
from application.course_service import CourseService
from domain.course import Course
from infrastructure.mongodb import get_engine

router = APIRouter()


async def get_course_service(request: Request) -> CourseService:
    engine = get_engine(request.app)
    return CourseService(engine)


@router.post('/courses/', response_model=Course)
async def create_course(
    course: Course,
    service: CourseService = Depends(get_course_service),
    current_user: dict = Depends(get_current_user),
):
    try:
        if course.teacher_id is not None:
            course.teacher_id = ObjectId(course.teacher_id)
        return await service.create_course(course)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/courses/', response_model=List[GetCourseDTO])
async def list_course(
    service: CourseService = Depends(get_course_service),
    current_user: dict = Depends(get_current_user),
):
    courses = await service.list_course()
    return [
        GetCourseDTO(
            course_id=str(course.course_id),
            course_name=course.course_name,
            course_type=course.course_type,
            course_intro=course.course_intro,
            course_outline=course.course_outline,
            course_price=course.course_price,
            course_image=course.course_image,
            teacher_id=str(course.teacher_id),
            students=str(course.students),
            course_content=course.course_content,
        )
        for course in courses
    ]


@router.get('/courses/{course_id}', response_model=Course)
async def get_course(
    course_id: str,
    service: CourseService = Depends(get_course_service),
    current_user: dict = Depends(get_current_user),
):
    course = await service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')
    return course


@router.delete('/courses/{course_id}')
async def delete_course(
    course_id: str,
    service: CourseService = Depends(get_course_service),
    current_user: dict = Depends(get_current_user),
):
    success = await service.delete_course(course_id)
    if not success:
        raise HTTPException(status_code=404, detail=f'Course with ID {course_id} not found')
    return {'message': f'Course with ID {course_id} deleted successfully'}


@router.patch('/courses/{course_id}', response_model=Course)
async def patch_course(
    course_id: str,
    course_data: dict,
    service: CourseService = Depends(get_course_service),
    current_user: dict = Depends(get_current_user),
):
    try:
        course = await service.patch_course(course_id, course_data)
        if not course:
            raise HTTPException(status_code=404, detail='Course not found')
        return course
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
