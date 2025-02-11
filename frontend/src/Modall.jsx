import './Modall.css'
function Modal({ title, fullStory, image, onClose }) {
    return (
      <div className="modal">
        <div className="modalcontent">
          <button className="closebutton" onClick={onClose}>
            &times;
          </button>
          <div className="image">
          <img src={image} alt={title} />
          </div>
          <h3>{title}</h3>
          <p>{fullStory}</p>
        </div>
      </div>
    )
  }
  
  export default Modal