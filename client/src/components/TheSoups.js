import React from "react";
import SoupCard from "./SoupCard";

function TheSoups({soups}){
    const theSoups = soups.map((soup) => 
    <SoupCard
        key={soup.id}
        name={soup.name}
        image={soup.image}
        id={soup.id}
    />
    )
    return (
        <div className='grid grid-cols-3 md:grid-cols-3 gap-10'>{theSoups}</div>
    )

}
export default TheSoups