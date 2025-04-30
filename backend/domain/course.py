from odmantic import Model, Field
from typing import Optional, List
from bson import ObjectId
from datetime import datetime

# 章節檔案
class ChapterFile(Model):
    filename: str
    url: str

# 章節
class Chapter(Model):
    chapter_id: Optional[ObjectId] = None
    chapter_name: str
    chapter_file: List[ChapterFile]  # 章節文件列表

class Course(Model):
    course_id: Optional[ObjectId] = Field(primary_field=True, default_factory=ObjectId)  # 自動生成隨機 ID
    course_name: str
    course_type: str
    course_intro: str
    course_outline: str
    course_image: str
    course_price: int
    course_content: List[Chapter]
    create_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())  # 自動生成創建時間
    last_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())  # 自動生成最後更新時間
    teacher_id: Optional[ObjectId] = None