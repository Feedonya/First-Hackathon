import React, { useEffect, useState } from 'react'
import { Button } from '@mui/material'
import './App.css'
import Navbar from "./components/Navbar/Navbar"
import HomePage from "./pages/HomePage/HomePage"
import ProfilePage from './pages/ProfilePage/ProfilePage'
import CoursesPage from './pages/CoursesPage/CoursesPage'
import MyCoursesPage from './pages/MyCoursesPage/MyCoursesPage'
import LeaderboardPage from './pages/LeaderboardPage/LeaderboardPage'
import { HomeRounded, SchoolRounded, LeaderboardRounded } from '@mui/icons-material'

const App = () => {
  const [tab, setTab] = useState("Курсы")
  const [user, setUser] = useState({
    id: 1,
    role: 1,
    username: "gryazniy_abobus228",
    password: "jopaspisey228"
  })

  /*useEffect(() => {
    const handleUserChanged = () => {
      setUser(fetch(null))
    }
  })*/

  const testUser = {
    id: 1,
    role: 1,
    username: "gryazniy_abobus228",
    password: "jopaspisey228"
  }

  const handleAuth = () => {
    alert("Never gonna give you up")
  }

  return (
    <>
      <Navbar current={tab} 
              onClick={setTab} 
              tabs={[["Главная", <HomeRounded />], ["Курсы", <SchoolRounded />], ["Лидерборды", <LeaderboardRounded />]]}
              sessionUser={user}
              handleAuth={handleAuth}/>
      <pre>{tab}</pre>
      <main>
      { tab === "Главная" && <HomePage /> }
      { tab === "Курсы" && <CoursesPage /> }
      { tab === "Лидерборды" && <LeaderboardPage /> }
      { tab === "Мой профиль" && <ProfilePage /> }
      { tab === "Мои курсы" && <MyCoursesPage /> }
      </main>
      
    </>
  )
}

export default App
