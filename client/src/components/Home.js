import React from "react"
import { useState } from "react";
import { useHistory } from "react-router-dom";



export default function Home() {
  const [fadeOut, setFadeOut] = useState(false);
  const history = useHistory();


  const handleFadeOut = () => {
    setFadeOut(true);
  };

  const handleNavigateToSoups = () => {
    setFadeOut(true);
    setTimeout(() => {
    history.push("/thesoups");} // Navigate to the /thesoups route
, 400);}

  return (
    <>
      <div id="switchbody" className={`transition-opacity duration-500 ${
        fadeOut ? "opacity-0 pointer-events-none" : "opacity-100"
      }`}
      onClick={handleNavigateToSoups}
      >
        <div id="switchn" class="nintendo">
          <div id="switchns" class="nintendo-switch">
            <div id="switchnsl" class="left"></div>
            <div id="switchnsr" class="right"></div>
          </div>
        </div>
        <h1 id="switchh1">Nintendo</h1>
        <h2 id="switchh2">Soup</h2>
      </div>
    </>
  )
}