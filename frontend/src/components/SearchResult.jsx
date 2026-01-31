import React from "react";
import VideoCard from './VideoCard.jsx'

const SearchResult = ({ input }) => {
    return (
        <div className="search-result p-5">
            {(input || []).map((title) => (
                <VideoCard title={title} />
            ))}
        </div>
    )
};


export default SearchResult;






