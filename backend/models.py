from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from dbconfig import meta

QuestionSet = Table("questions_set", meta,
                Column("question_set_id", Integer, primary_key=True),
                Column("question_set_title", String(45)),
                Column("question_set_order", Integer, unique=True)
                )

Question = Table("questions", meta,
            Column("question_id", Integer, primary_key=True),
            Column("question_text", String(100)),
            Column("question_set_id", Integer, ForeignKey("questions_set.question_set_id"))
            )


Option = Table("options", meta,
            Column("option_id", Integer, primary_key=True),
            Column("option_text", String(100)),
            Column("question_id", Integer, ForeignKey("questions.question_id"))
            )

Answer = Table("answers", meta,
            Column("answer_id", Integer, primary_key=True),
            Column("option_id", Integer, ForeignKey("options.option_id"))
            )
