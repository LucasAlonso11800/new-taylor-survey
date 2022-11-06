export type QuestionSet = {
    question_set_id: number
    question_set_order: number
    question_set_title: string
}

export type Question = {
    question_id: number
    question_text: string
}

export type Option = {
    option_id: number
    option_text: string
}

export type QuestionResponse = {
    error: boolean
    message: string
    data: {
        options: Option[]
        questionSet: QuestionSet
        questions: Question[]
    }
}