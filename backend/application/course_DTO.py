from pydantic import BaseModel


class GetCourseDTO(BaseModel):
    course_id: str
    course_name: str
    course_type: str
    course_intro: str
    course_outline: str
    course_price: int
    course_image: str
    # teacher_id: str
