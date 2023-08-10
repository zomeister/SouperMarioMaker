import Button from './Button'
import React from 'react'

export default function SoupCard(theSoups) {


    function submitOrder(e) {
        console.log('submitOrder');
    }
    
    const card = 
    <div>
        <img className='soup-pic' src={theSoups.image} height={300} width={300} alt={theSoups.name}></img>
        <p className='soup-name'>{theSoups.name}</p>

    </div>
    
    return (
        <div className='soup-card'>
            {card}
            <Button
                handleClick={(e) => submitOrder(e)}
                text={"ORDER UP!"}    
            ></Button>
        </div>
    )
}