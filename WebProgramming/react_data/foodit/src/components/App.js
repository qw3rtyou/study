import FoodList from "./FoodList";
import items from "../mock.json";

function App() {
  return (
    <div>
      <button>최신순</button>
      <button>칼로리순</button>
      <FoodList items={items} />
    </div>
  );
}

export default App;
