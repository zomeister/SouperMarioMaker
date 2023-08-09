import React, { useEffect, useState } from "react";
import Button from "./Button";
import FavoriteSoups from "./FavoriteSoups";
import IngredientCard from "./IngredientCard";
import Menu from "./Menu";
import SoupCard from "./SoupCard";
import { Switch, Route} from "react-router-dom";
import { BrowserRouter } from "react-router-dom/cjs/react-router-dom.min";
import Header from "./Header";

function App() {
  // const [soups, setSoups] = useState(null);
  const [ingredients, setIngredients] = useState([]);

  useEffect(() => {
    fetchIngredients();
  }, []);

  function fetchIngredients() {
    fetch('http://localhost:5555/ingredients')
    .then((res) => res.json())
    .then((ingredients) => setIngredients(ingredients))
  }
  console.log(ingredients);

  const [soups, setSoups] = useState([])

  useEffect(() => {
    fetchAllSoups();
  }, []);

  function fetchAllSoups() {
  fetch('http://localhost:5555/soups')
  .then(res => res.json())
  .then(soups => setSoups(soups))
  console.log(soups)
  }

  return ( <BrowserRouter>
  <>
      <div className="App">
      </div>
      <div className="App2">
      <h1 id="head"><a id='heada' href="#0" className="font-mario font-normal text-blue-200 text-lg">SOUPER MARIO MAKER</a></h1>
        <Switch>
          <Route exact path="/">
            <Header/>
           <Menu ingredients={ingredients}/>
          </Route>
          <Route path="/favoritesoup">
            <FavoriteSoups soups={soups}/>
          </Route>
        </Switch>
      </div>
  </>
  </BrowserRouter>
  )
}



export default App;
