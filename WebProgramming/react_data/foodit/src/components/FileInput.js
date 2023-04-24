import { useRef, useState, useEffect } from "react";

function FileInput({ name, value, onChange }) {
  const inputRef = useRef();
  const [preview, setPreview] = useState();

  const handleChange = (e) => {
    const nextValue = e.target.files[0];
    onChange(name, nextValue);
  };

  const handleClearClick = () => {
    const inputNode = inputRef.current;
    if (!inputNode) return;
    inputNode.value = null;
    onChange(name, null);
  };

  useEffect(() => {
    if (value == null) return;

    const nextPreview = URL.createObjectURL(value);
    setPreview(nextPreview);

    return () => {
      setPreview();
      URL.revokeObjectURL(preview);
    };
  }, [value]);

  return (
    <div>
      <img src={preview} alt="이미지 미리보기" />
      <input type="file" onChange={handleChange} />
      <button type="button" onClick={handleClearClick} ref={inputRef}>
        X
      </button>
    </div>
  );
}

export default FileInput;
