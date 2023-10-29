import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import Footer from "./containers/footer/footer.jsx";
import Navbar from "./components/navbar/navbar.jsx";
import Home from "./containers/home/home.jsx"
import Login from "./containers/login/login.jsx"
import Content from "./containers/content/content.jsx"

function App() {

  return (
    <>
        <Router>
            <Navbar />

            <Routes>
                <Route path="/" exact element={<Home/>} />
                <Route path="/login" element={<Login/>} />
                <Route path="/content" element={<Content/>} />
            </Routes>
            <Footer />

        </Router>
    </>
  )
}

export default App
