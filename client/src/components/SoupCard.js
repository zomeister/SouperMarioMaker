import Button from './Button'

export default function SoupCard({ingredients = null}) {


    function submitOrder(e) {
        console.log('submitOrder');
    }

    return (
        <div>
            <h1>Soup Card</h1>
            <p>image</p>
            <Button
                handleClick={(e) => submitOrder(e)}
                text={"ORDER UP!"}    
            ></Button>
        </div>
    )
}