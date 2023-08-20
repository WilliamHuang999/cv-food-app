import './App.css';
import React, {useRef, useEffect, useState} from "react";
//import { BrowserRouter as Router, Switch, Route, Redirect, } from 'react-router-dom';
import {Routes, Route, useNavigate} from 'react-router-dom';
import * as tf from '@tensorflow/tfjs';
//import {loadGraphModel} from '@tensorflow/tfjs-converter';

//import Pagex from"./components/Pagex"



export default function App() {  
  return (

      <Routes>
          <Route path="/pagex" element={<Pagex />} />
          <Route path="/" element={<Home />}/>
      </Routes>
  );
}


const Home = () => {
        const navigate = useNavigate();
      
        const videoRef = useRef(null);
        const photoRef = useRef(null);
        
        const [hasPhoto, setHasPhoto] = useState(false);
      
        const getVideo = () => {
          navigator.mediaDevices
          .getUserMedia({ video: { width: 720, height: 720}})
          .then(stream => {
            let video = videoRef.current;
            video.srcObject = stream;
            video.play();
          })
          .catch(err => {
              console.error(err);
          })
        }
      
        const navigateToPagex = () => {
          navigate('/pagex');
        }
      
        const takePhoto = () => {
      {/*      const width = 414;
            const height = width / (16/9);
        */}
            const width = 720;
            const height = 720;
            let video = videoRef.current;
            let photo =  photoRef.current;
      
            photo.width = width;
            photo.height = height;
      
            let ctx = photo.getContext('2d');
            
            ctx.drawImage(video, 0,0,width,height);
            setHasPhoto(true);
      
        }
      
        const closePhoto = () => {
          let photo = photoRef.current;
          let ctx = photo.getContext('2d');
      
          ctx.clearRect(0,0,photo.width, photo.height);
      
          setHasPhoto(false);
        }
      
        useEffect(() => {
          getVideo();
        }, [videoRef]);
      
      
        let props = {
          photoRef : photoRef,
          hasPhoto : hasPhoto,
          closePhoto : closePhoto,
          videoRef : videoRef,
          takePhoto : takePhoto
        }
      
        return(
          <div className=".App">
            <div className="camera">
              <video ref={videoRef}>
      
              </video>
            </div>
            <button type="button" onClick={navigateToPagex} className="snapButton">SNAP!</button>
              {/*Passing photoRef prop to Pagex component*/}
              <Pagex {...props} />
          </div>
        );
}
 
function Pagex(props){
  const navigate = useNavigate();
  const navigateHome = () => {
    navigate('/');
  }

  return(
    <div className="anotherTwo">
        <button type="button" onClick={navigateHome} className="returnButton">Return</button>
    </div>
  );  
}


//const MODEL_PATH = '/home/kpan/test2/model.json';

//const model = await loadGraphModel(MODEL_PATH);
//const cat = document.getElementById('cat');
//model.execute(tf.browser.fromPixels(cat));



