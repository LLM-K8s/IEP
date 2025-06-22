from typing import List

from bson import ObjectId
from odmantic import AIOEngine
from pydantic import ValidationError

from domain.course import Course


class CourseService:
    def __init__(self, engine: AIOEngine):
        self.engine = engine

    async def create_course(self, course: Course) -> Course:
        try:
            await self.engine.save(course)
            return course
        except ValidationError as e:
            raise ValueError(f'課程資料驗證失敗: {e}')

    async def list_course(self) -> List[Course]:
        return await self.engine.find(Course, {})

    async def get_course(self, course_id: str) -> Course | None:
        try:
            object_id = ObjectId(course_id)
            return await self.engine.find_one(Course, Course.course_id == object_id)
        except:  # noqa: E722
            return None

    async def delete_course(self, course_id: str) -> bool:
        try:
            object_id = ObjectId(course_id)
            course = await self.engine.find_one(Course, Course.course_id == object_id)
            if course:
                await self.engine.delete(course)
                return True
            return False
        except:  # noqa: E722
            return False

    async def patch_course(self, course_id: str, course_data: dict) -> Course | None:
        try:
            object_id = ObjectId(course_id)
            course = await self.engine.find_one(Course, Course.course_id == object_id)
            if course:
                for key, value in course_data.items():
                    setattr(course, key, value)
                await self.engine.save(course)
                return course
            return None
        except ValidationError as e:
            raise ValueError(f'課程資料驗證失敗: {e}')
        except Exception as e:
            raise ValueError(f'更新課程失敗: {e}')
