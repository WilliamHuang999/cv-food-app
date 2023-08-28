import React, {useRef, useEffect, useState, Fragment } from "react";
import * as tf from "@tensorflow/tfjs";
import { DropzoneArea } from "material-ui-dropzone";
import {Backdrop, Chip, CircularProgress, Grid, Stack } from "@mui/material";


function Upload(){
    {/*Set up component states*/}
    const [model, setModel] = useState(null);
    const [classLabels, setClassLabels] = useState(null);
    const [loading, setLoading] = useState(false);
    const [confidence, setConfidence] = useState(null);
    const [predictedClass, setPredictedClass] = useState(null);

    {/*Load the model and fetch the labels*/}
    useEffect(() => {
        const loadModel = async () => {
            const model_url = "test/model.json";

            const model = await tf.loadGraphModel(model_url);
            setModel(model);
            console.log("Upload model loaded");
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
    }, []);



    const readImageFile = (file) => {
        return new Promise((resolve) => {
            const reader = new FileReader();

            reader.onload = () => resolve(reader.result);

            reader.readAsDataURL(file);
        });
    };

    const createHTMLImageElement = (imageSrc) => {
        return new Promise((resolve) => {
            const img = new Image();

            img.onload = () => resolve(img);

            img.src = imageSrc;
        });
    };


    const handleImageChange = async (files) => {
        if (files.length === 0){
            setConfidence(null);
            setPredictedClass(null);
        }

        if (files.length === 1){
            setLoading(true);

            const imageSrc = await readImageFile(files[0]);
            const image = await createHTMLImageElement(imageSrc);

            {/*tf.tidy for automatic memory cleanup*/}
            const [predictedClass, confidence] = tf.tidy(() => {
                const tensorImg = tf.browser.fromPixels(image).resizeNearestNeighbor([224, 224]).toFloat().expandDims();
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
            setLoading(false);
        }
    };

    return(
        <Fragment>
            <Grid container className="App" direction="column" alignItems="center" justifyContent="center" marginTop="12%">
                <Grid item>
                    <h1 style={{ textAlign: "center", marginBottom: "1.5em" }}>Image Classifier</h1>
                 <DropzoneArea
                    acceptedFiles={["image/*"]}
                    dropzoneText={"Add an image"}
                    onChange={handleImageChange}
                    maxFileSize={10000000}
                    filesLimit={1}
                    showAlerts={["error"]}
                />
                {/*Lists the top 5 guesses. Only guesses with nonzero confidence are displayed*/}
                      <Stack style={{ marginTop: "2em", width: "20rem" }} direction="column" spacing={1}>
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
                </Grid>
            </Grid>

              <Backdrop sx={{ color: "#fff", zIndex: (theme) => theme.zIndex.drawer + 1}} open={loading}>
                <CircularProgress color="inherit" />
              </Backdrop>
        </Fragment>
    );
}

export default Upload;