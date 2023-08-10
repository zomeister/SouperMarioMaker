import React from "react"
import { useState } from "react";

export default function Home() {
  const [fadeOut, setFadeOut] = useState(false);

  const handleFadeOut = () => {
    setFadeOut(true);
  };

  return (
    <>
      <div id="switchbody" className={`transition-opacity duration-500 ${fadeOut ? "opacity-0 pointer-events-none" : "opacity-100"
        }`}
      /*onClick={handleFadeOut}*/>
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