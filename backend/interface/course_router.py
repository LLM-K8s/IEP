from fastapi import APIRouter, HTTPException, Depends
from typing import List
from domain.course import Course
from application.course_service import CourseService
from infrastructure.mongodb import get_engine

router = APIRouter()

async def get_course_service() -> CourseService:
    engine = get_engine()
    return CourseService(engine)

@router.post("/courses/", response_model=Course)
async def create_course(course: Course, service: CourseService = Depends(get_course_service)):
    return await service.create_course(course)

@router.get("/courses/", response_model=List[Course])
async def list_course(service: CourseService = Depends(get_course_service)):
    return await service.list_course()

@router.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: str, service: CourseService = Depends(get_course_service)):
    course = await service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.delete("/courses/{course_id}")
async def delete_course(course_id: str, service: CourseService = Depends(get_course_service)):
    success = await service.delete_course(course_id)
    if not success:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}