import React, {useRef, useEffect, useState} from "react";
import * as tf from "@tensorflow/tfjs";
import {Chip, Stack } from "@mui/material";

function Camera() {
  {/*Photo and video components*/}
  const videoRef = useRef(null);
  const photoRef = useRef(null);
  const [hasPhoto, setHasPhoto] = useState(false);

  {/*Model components*/}
  const [model, setModel] = useState(null);
  const [classLabels, setClassLabels] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [predictedClass, setPredictedClass] = useState(null);

  {/*Load model and fetch the labels*/}
  useEffect(() => {
    const loadModel = async () => {
        const model_url = "test/model.json";

        const model = await tf.loadGraphModel(model_url);
        setModel(model);
        console.log("Camera model loaded");
    };

    const getClassLabels = async () => {
        const res = await fetch(
            "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
            
        );

        const data = await res.json();
        setClassLabels(data);
    };
    loadModel();
    getClassLabels();
    getVideo();
  }, [videoRef]);


  {/*Set up video component. DOMException error with video.play() because after first execution, video is still playing when on another page, and
switching back causes this function to trigger another load video request.*/}
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



  {/*Take the photo and make predictions*/}
  const takePhoto = async () => {
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
      {/*tf.tidy for automatic memory cleanup*/}
      const [predictedClass, confidence] = tf.tidy(() => {
        const tensorImg = tf.browser.fromPixels(photo).resizeNearestNeighbor([224, 224]).toFloat().expandDims();
        const result = model.predict(tensorImg);

        const predictions = Array.from(result.dataSync());
        const {values, indices} = tf.topk(predictions, 5);
        const top5Values = Array.from(values.dataSync());
        const top5Indices = Array.from(indices.dataSync());

        const predictedClass = [];
        for (let i = 0; i < 5; i++){
          predictedClass[i] = classLabels[top5Indices[i]];
        }
        const confidence = [];
        for (let i = 0; i < 5; i++){
          confidence[i] = Math.round(top5Values[i] * 100);
        };

        return [predictedClass, confidence];
      });
      setPredictedClass(predictedClass);
      setConfidence(confidence);
  }


  const closePhoto = () => {
    let photo = photoRef.current;
    let ctx = photo.getContext('2d');

    ctx.clearRect(0,0,photo.width, photo.height);

    setHasPhoto(false);
  }
{/*
  useEffect(() => {
    getVideo();
  }, [videoRef]);*/}


  return (
		// Maybe use wrapping div instead of fragment
    <>
      <div className="camera">
          <video ref={videoRef}></video>
          <button onClick={takePhoto}>SNAP!</button>
      </div>
      <div className={"result" + (hasPhoto ? 'hasPhoto': '')}>
        <canvas ref={photoRef}></canvas>
        <button onClick={closePhoto}>CLOSE!</button>

      {/*Could clean this up using a for loop*/}
      {/*Lists the top 5 guesses. Only nonzero guesses will be listed*/}
        <Stack style={{ marginTop: "2em", marginLeft: "2em", marginBottom: "2em", width: "20rem" }} direction="column" spacing={1}>
              <Chip
                  label={confidence === null ? "1." : '1. ' +predictedClass[0] + ' (' + confidence[0]+'%)'}
                  style={{ justifyContent: "left" }}
                  variant="outlined"
              />
              <Chip
                  label={confidence === null || confidence[1] === 0 ? "2." : '2. '+predictedClass[1] + ' (' + confidence[1]+'%)'}
                  style={{ justifyContent: "left" }}
                  variant="outlined"
              />
              <Chip
                  label={confidence === null || confidence[2] === 0 ? "3." : '3. '+predictedClass[2] + ' (' + confidence[2]+'%)'}
                  style={{ justifyContent: "left" }}
                  variant="outlined"
              />
              <Chip
                  label={confidence === null || confidence[3] === 0 ? "4." : '4. '+predictedClass[3] + ' (' + confidence[3]+'%)'}
                  style={{ justifyContent: "left" }}
                  variant="outlined"
              />
              <Chip
                  label={confidence === null || confidence[4] === 0? "5." : '5. '+predictedClass[4] + ' (' + confidence[4]+'%)'}
                  style={{ justifyContent: "left" }}
                  variant="outlined"
              />
        </Stack>
        </div>
    </>
  );
}

export default Camera;