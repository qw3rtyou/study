import FoodList from "./FoodList";
//import mockItems from "../mock.json";
import { useState, useEffect } from "react";
import { getFoods } from "../api";

function App() {
  const [order, setOrder] = useState("createdAt");
  const [items, setItems] = useState([]);

  const handleNewestClick = () => setOrder("createdAt");
  const handleCalorieClick = () => setOrder("calorie");
  const sortedItems = items.sort((a, b) => b[order] - a[order]);
  const handleDelete = (id) => {
    setItems(items.filter((item) => item.id !== id));
  };

  const handleLoad = async (queryOrder) => {
    const { foods } = await getFoods(queryOrder);
    setItems(foods);
  };

  useEffect(() => {
    handleLoad(order);
  }, [order]);

  return (
    <div>
      <button onClick={handleNewestClick}>최신순</button>
      <button onClick={handleCalorieClick}>칼로리순</button>
      <FoodList items={sortedItems} onDelete={handleDelete} />
    </div>
  );
}

export default App;
