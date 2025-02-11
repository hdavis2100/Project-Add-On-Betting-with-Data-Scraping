import './NFLGame.css'
function NFLGame({ game }) {
    const { home_team, away_team, commence_time, bookmakers } = game;
  
    const commenceTime = new Date(commence_time);
    const unibet = bookmakers?.[0];
    const moneylineMarket = unibet?.markets?.[0];
    const homeOdds = moneylineMarket?.outcomes?.find((outcome) => outcome.name === home_team)?.price;
    const awayOdds = moneylineMarket?.outcomes?.find((outcome) => outcome.name === away_team)?.price;
    const oddsColor = (price) => (price > 0 ? "positive" : "negative");
    if (!moneylineMarket) return null;
  
    return (
      
        <div className="gameodds">
        <p>
          <strong>{home_team}</strong> vs. <strong>{away_team}</strong>: {commenceTime.toLocaleString()}
        </p>
        {homeOdds && (
        <p>
          <p><strong>Moneyline Odds (Unibet):</strong> {home_team}: <span className={oddsColor(homeOdds)}> <bold>{homeOdds> 0 ? `+${homeOdds}` : homeOdds}</bold></span> 
         </p>
        </p>
        
        )}
        {awayOdds && (
        <p>
          <p><strong>Moneyline Odds (Unibet):</strong> {away_team}: <span className={oddsColor(awayOdds)}> <bold>{awayOdds> 0 ? `+${awayOdds}` : awayOdds}</bold></span> 
         </p>
        </p>
        )}
        </div>
      
    );
  }
  
  export default NFLGame;