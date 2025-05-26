from datetime import datetime
from typing import List, Optional

from bson import ObjectId
from odmantic import Field, Model


# 章節檔案
class ChapterFile(Model):
    filename: str
    url: str


# 章節
class Chapter(Model):
    chapter_name: str
    chapter_file: List[ChapterFile]  # 章節文件列表


# 課程
class Course(Model):
    course_id: Optional[ObjectId] = Field(
        primary_field=True, default_factory=ObjectId
    )  # 自動生成隨機 ID  # noqa: E501
    course_name: str
    course_type: str
    course_intro: str
    course_outline: str
    course_image: str
    course_price: int
    course_content: List[Chapter]
    create_at: datetime = Field(
        default_factory=lambda: datetime.utcnow().astimezone(tz=None)
    )  # UTC  # noqa: E501
    last_at: datetime = Field(default_factory=lambda: datetime.utcnow().astimezone(tz=None))
    teacher_id: Optional[ObjectId]
    students: List[ObjectId]
