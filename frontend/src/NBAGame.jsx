import './NBAGame.css';
function NBAGame({ game }) {
    
    const { home_team, away_team, commence_time, scores } = game;
    const commenceTime = new Date(commence_time);
  
    return (
      
        <div className="game">
        <p>
          <strong>{home_team}</strong> vs. <strong>{away_team}</strong>
        </p>
        <p>{commenceTime.toLocaleString()}</p>
        
        {scores && (
          <p>
            <strong>{scores[0].name}</strong> {scores[0].score} - <strong>{scores[1].name}</strong> {scores[1].score}
          </p>
        )}
        </div>
      
    );
  }
  
  export default NBAGame;