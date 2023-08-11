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
  const [ingredients, setIngredients] = useState([]) 
  const [soups, setSoups] = useState([]);
  const [soupIngredients, setSoupIngredients] = useState([]);

  const [soup, setSoup] = useState(null);

  useEffect(() => {
    fetch('http://localhost:3000/ingredients')
    .then((res) => res.json())
    .then((ingredients) => setIngredients(ingredients))

    fetch('http://localhost:3000/soups')
    .then(res => res.json())
    .then(soups => setSoups(soups))

    fetch('http://localhost:3000/soup_ingredients')
    .then(res => res.json())
    .then(soupIngredients => setSoupIngredients(soupIngredients))

    fetch('http://localhost:3000/soups/1')
    .then(res => res.json())
    .then(soup => setSoup(soup))
  }, []);

  // function submitOrder(ai) { // post to soups
  //   fetch(`http://localhost:3000/soup_ingredients`)
  //   .then(res => res.json())
  //   .then(()=>{})
  // }

  function addSoupIngredient() { // post to soup_ingredients

  }

  return ( <BrowserRouter>
  <>
      <div className="App">
      </div>
      <div className="App2">
      <h1 id="head"><a id='heada' href="#0" className="font-mario font-normal text-lg">SOUPER MARIO MAKER</a></h1>
        <Switch>
          <Route exact path="/">
            <Header/>
           <Menu soup={soup} ingredients={ingredients} soupIngredients={soupIngredients} />
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
