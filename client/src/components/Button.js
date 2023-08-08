export default function Button({text = 'Click Me!', handleClick}) {

    return (
        <button onClick={handleClick}>{text}</button>
    )
}