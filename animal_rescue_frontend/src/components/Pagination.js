import React from "react";

const Pagination = ({PostsPerPage, totalPosts, paginate}) =>{
    const pageNumbers = [];
    for(let i = 1; i <= Math.ceil(totalPosts / PostsPerPage); i++){
        pageNumbers.push(i);
    }
    return(
        <navbar className='navbar'>
            <ul className='pagination'>
                {pageNumbers.map(number => (
                    <li key={number} className='page-item'>
                        <a onClick={() => paginate(number)} href='!#' className='page-link'>{number}</a>
                    </li>
                ))}
            </ul>
        </navbar>
    )
}

export default Pagination