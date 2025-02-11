import './Article.css'
function Article({ title, content, image, onClick }) {
    return (
      <div className="article" onClick={onClick}>
        <img src={image} alt={title} className="articleimage" />
        <h4>{title}</h4>
        <p>{content}</p>
      </div>
    )
  }
  
  export default Article