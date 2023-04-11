import { useState } from "react";
import "./ReviewForm.css";
import FileInput from "./FileInput.js";

function ReviewForm() {
  const [values, setValue] = useState({
    title: "",
    rating: 0,
    content: "",
    imgFile: null,
  });

  const handleChange = (name, value) => {
    setValue((preValue) => ({
      ...preValue,
      [name]: value,
    }));
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    handleChange(name, value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(values);
  };

  return (
    <form className="ReviewForm" onSubmit={handleSubmit}>
      <FileInput
        name="imgFile"
        value={values.imgFile}
        onChange={handleChange}
      />
      <input
        name="title"
        value={values.title}
        onChange={handleInputChange}
      ></input>
      <input
        type="number"
        name="rating"
        value={values.rating}
        onChange={handleInputChange}
      ></input>
      <textarea
        name="content"
        value={values.content}
        onChange={handleInputChange}
      ></textarea>
      <button type="submit">확인</button>
    </form>
  );
}

export default ReviewForm;
