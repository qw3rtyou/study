const BASE_URL = "https://learn.codeit.kr/api/film-reviews";

export async function getReviews({
  order = "createdAt",
  offset = 0,
  limit = 6,
}) {
  const query = "order=" + order + "&offset=" + offset + "&limit=" + limit;
  const response = await fetch(`${BASE_URL}?${query}`);

  if (!response.ok) {
    throw new Error("리뷰를 가져오는데 실패했습니다");
  }

  const body = await response.json();
  return body;
}

export async function createReviews(formData) {
  const response = await fetch(`${BASE_URL}`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("리뷰를 생성하는데 실패했습니다");
  }

  const body = await response.json();
  return body;
}
