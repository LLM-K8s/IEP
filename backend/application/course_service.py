from typing import List
from odmantic import AIOEngine
from domain.course import Course
from bson import ObjectId

class CourseService:
    def __init__(self, engine: AIOEngine):
        self.engine = engine
    async def create_course(self, course: Course) -> Course:
        await self.engine.save(course)
        return course
    async def list_course(self) -> List[Course]:
        return await self.engine.find(Course, {})
    async def get_course(self, course_id: str) -> Course | None:
        try:
            object_id = ObjectId(course_id)
            return await self.engine.find_one(Course, Course.id == object_id)
        except:
            return None
    async def delete_course(self, course_id: str) -> bool:
        try:
            object_id = ObjectId(course_id)
            course = await self.engine.find_one(Course, Course.id == object_id)
            if course:
                await self.engine.delete(course)
                return True
            return False
        except:
            return False