import React, { useEffect, useState } from "react";
import Button from "./Button";
import FavoriteSoups from "./FavoriteSoups";
import IngredientCard from "./IngredientCard";
import Menu from "./Menu";
import SoupCard from "./SoupCard";
import { Switch, Route, Routes} from "react-router-dom";

function App() {
  // const [soups, setSoups] = useState(null);
  const [ingredients, setIngredients] = useState([]);

  useEffect(() => {
    fetchIngredients();
  }, []);

  function fetchIngredients() {
    fetch('/api/ingredients')
    .then(res => res.json())
    .then(data => setIngredients(data))
    .catch(err => console.log(err));
    console.log(ingredients);
  }

  // function fetchAllSoups() {
  //   fetch('/api/soups')
  //  .then(res => res.json())
  //  .then(data => setSoups(data))
  //  .catch(err => console.log(err));
  // }

  return <h1>{<Menu ingredients={ingredients}/>}</h1>;
}

function Home() {
  return <h1>Home</h1>;
}

function Soupify() {
  return <h1>Soupify</h1>;
}

function FinalSoup() {
  return <h1>FinalSoup</h1>;
}

function NavBar() {

}


export default App;
