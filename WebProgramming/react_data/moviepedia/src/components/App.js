import ReviewList from "./ReviewList";
//import mockItems from "../mock.json";
import { useEffect, useState } from "react";
import { getReviews } from "../api";
import ReviewForm from "./ReviewForm";

const LIMIT = 6;

function App() {
  const [order, setOrder] = useState("createdAt");
  const [items, setItems] = useState([]);
  const [offset, setOffset] = useState(0);
  const [hasNext, setHasNext] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [loadingError, setLoadingError] = useState(null);

  const sortedItems = items.sort((a, b) => b[order] - a[order]);

  const handleNewestClick = () => setOrder("createdAt");

  const handleBestClick = () => setOrder("rating");

  const handleDelete = (id) => {
    setItems(items.filter((item) => id !== item.id));
  };
  const handleLoad = async (options) => {
    let result;

    try {
      setIsLoading(true);
      result = await getReviews(options);
    } catch (error) {
      setLoadingError(error);
    } finally {
      setIsLoading(false);
    }

    const { reviews, paging } = result;

    if (options.offset === 0) {
      setItems(reviews);
    } else {
      setItems((prevItems) => [...prevItems, ...reviews]);
    }
    setOffset(options.offset + reviews.length);
    setHasNext(paging.hasNext);
  };
  const handleLoadMore = () => {
    handleLoad({ order, offset, limit: LIMIT });
  };

  useEffect(() => {
    handleLoad({ order, offset: 0, limit: LIMIT });
  }, [order]);

  return (
    <div>
      <div>
        <button onClick={handleNewestClick}>최신순</button>
        <button onClick={handleBestClick}>베스트순</button>
      </div>
      <ReviewForm />
      <ReviewList items={sortedItems} onDelete={handleDelete} />
      {hasNext && (
        <button onClick={handleLoadMore} disabled={isLoading}>
          더보기
        </button>
      )}
      {loadingError?.message && <span>{loadingError.message}</span>}
    </div>
  );
}

export default App;
