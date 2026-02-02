import React from "react";
import VideoCard from './VideoCard.jsx'

const SearchResult = ({ data }) => {
    return (
        <div className="search-result p-5">
            {(data).map((video) => (
                <VideoCard key={video.id} video={video} />
            ))}
        </div>
    )
};


export default SearchResult;






