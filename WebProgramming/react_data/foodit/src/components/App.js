import FoodList from "./FoodList";
//import mockItems from "../mock.json";
import { useState, useEffect } from "react";
import { getFoods } from "../api";
import FoodForm from "./FoodForm";

function App() {
  const [order, setOrder] = useState("createdAt");
  const [items, setItems] = useState([]);
  const [cursor, setCursor] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [loadingError, setLoadingError] = useState(null);
  const [search, setSearch] = useState("");

  const sortedItems = items.sort((a, b) => b[order] - a[order]);

  const handleNewestClick = () => setOrder("createdAt");
  const handleCalorieClick = () => setOrder("calorie");
  const handleDelete = (id) => {
    setItems(items.filter((item) => item.id !== id));
  };
  const handleLoad = async (options) => {
    let result;
    try {
      setIsLoading(true);
      result = await getFoods(options);
    } catch (error) {
      setLoadingError(error);
    } finally {
      setIsLoading(false);
    }

    const { foods, paging } = result;
    if (options.cursor) {
      setItems((prevItems) => [...prevItems, ...foods]);
    } else {
      setItems(foods);
    }
    setCursor(paging.nextCursor);
  };

  const handleLoadMore = () => {
    handleLoad({ order, cursor });
  };

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    setSearch(e.target["search"].value);
  };

  useEffect(() => {
    handleLoad({ order, search });
  }, [order, search]);

  return (
    <div>
      <FoodForm />
      <form onSubmit={handleSearchSubmit}>
        <input name="search" />
        <button type="submit">검색</button>
      </form>
      <button onClick={handleNewestClick}>최신순</button>
      <button onClick={handleCalorieClick}>칼로리순</button>
      <FoodList items={sortedItems} onDelete={handleDelete} />
      {cursor && (
        <button onClick={handleLoadMore} disabled={isLoading}>
          더보기
        </button>
      )}
      {loadingError?.message && <span>{loadingError.message}</span>}
    </div>
  );
}

export default App;
