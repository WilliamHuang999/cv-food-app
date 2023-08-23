import FoodList from "./FoodList"
import React, {useRef, useEffect, useState} from "react";
import Navbar from './Navbar';
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import Camera from './Camera';

function App() {

  return (
    <>
    <Navbar />

    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/camera" element={<Camera />} />
    </Routes>
    </>

  );
}

export default App;
