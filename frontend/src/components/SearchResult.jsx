import React from "react";

const SearchResult = ({ input }) => {
  return (
    <ul className="p-5">
        <p>Results :</p>
      {(input || []).map((video) => (
        <li>
          {video}
        </li>
      ))}
    </ul>
  );
};


export default SearchResult;







