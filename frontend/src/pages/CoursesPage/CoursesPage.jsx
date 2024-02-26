import React from "react"
import style from "./CoursesPage.module.css"

const CoursePage = (props) => {
    const coursesList = [
        {
            id: 1,
            owner_id: 156,
            title: "Курс от Блиновской",
            is_open: true,
            category: ["Porno", "Milf", "Incest", "Taboo"]
        }, {
            id: 2,
            owner_id: 74,
            title: "Попаболь вышмат",
            is_open: true,
            category: ["Incest", "Dogs", "Zoo"]
        }, {
            id: 3,
            owner_id: 12,
            title: "СЕКС С ФИКСИКАМИ",
            is_open: false,
            category: ["Mults", "Moans", "Dogs"]
        }
    ]

    return (
    <section>
        <div className={style.searchBar}>
            
        </div>
    </section>
    )
}

export default CoursePage