import React from "react"
import style from "./CourseSearchCard.module.css"
import { Card, CardContent } from "@mui/material"

const CourseSearchCard = () => {
    return (
        <Card sx={{ minWidth: 275 }} className={style.}>
        <CardContent>
           
        </CardContent>
        <CardActions>
            <Button size="small">Перейти к курсу</Button>
        </CardActions>
        </Card>
    )
}

export default CourseSearchCard