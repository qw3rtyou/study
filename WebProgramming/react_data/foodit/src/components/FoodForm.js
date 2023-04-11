import { useState } from "react";

function FoodForm() {
  const [value, setValue] = useState({
    title: "",
    calorie: 0,
    content: "",
  });

  const handleValueChange = (e) => {
    const { name, value } = e.target;
    setValue((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <form>
      <input
        onChange={handleValueChange}
        value={value.title}
        name="title"
      ></input>
      <input
        onChange={handleValueChange}
        value={value.calorie}
        type="number"
        name="calorie"
      ></input>
      <input
        onChange={handleValueChange}
        value={value.content}
        name="content"
      ></input>
    </form>
  );
}

export default FoodForm;
