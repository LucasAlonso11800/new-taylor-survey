from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from dbconfig import meta

questions_sets = Table("questions_set", meta,
                Column("question_set_id", Integer, primary_key=True),
                Column("question_set_title", String(45)),
                Column("question_set_order", Integer, unique=True)
                )

questions = Table("questions", meta,
            Column("question_id", Integer, primary_key=True),
            Column("question_text", String(100)),
            Column("question_set_id", Integer, ForeignKey("questions_set.question_set_id"))
            )


options = Table("options", meta,
            Column("option_id", Integer, primary_key=True),
            Column("option_text", String(100)),
            Column("question_id", Integer, ForeignKey("questions.question_id"))
            )

answers = Table("answers", meta,
            Column("answer_id", Integer, primary_key=True),
            Column("option_id", Integer, ForeignKey("options.option_id"))
            )
