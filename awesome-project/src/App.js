import FoodList from "./FoodList"
import React, {useRef, useEffect, useState} from "react";
import Navbar from './Navbar';
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import Camera from './Camera';
import Upload from './Upload';
import Nutrition from "./Nutrition";

function App() {

  return (
    <>
    <Navbar />

    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/camera" element={<Camera />} />
      <Route path="/upload" element={<Upload />} />
      <Route path="/nutrition/" element={<Nutrition food="cheddar cheese"/>} />
    </Routes>
    </>

  );
}

export default App;
