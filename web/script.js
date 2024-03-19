document.addEventListener("DOMContentLoaded", function () {
  var currentGame = null;
  var currentPlayer = "white";
  var selectedSquare = null;

  function initializeChessboard() {
    var chessboard = document.getElementById("chessboard");
    for (var i = 0; i < 64; i++) {
      var square = document.createElement("div");
      square.className = "square";
      square.id = "square" + i;
      chessboard.appendChild(square);
      square.addEventListener("click", handleSquareClick);
    }
  }

  function handleSquareClick(event) {
    var squareId = event.target.id;
    var row = Math.floor(parseInt(squareId.substring(6)) / 8);
    var col = parseInt(squareId.substring(6)) % 8;
    var piece = currentGame.board[row][col];
    if (
      selectedSquare === null &&
      piece !== " " &&
      piece === currentPlayer.toLowerCase()
    ) {
      selectedSquare = { row: row, col: col };
      showValidMoves(row, col);
    } else if (selectedSquare !== null) {
      var isValidMove = isValidMove(
        selectedSquare.row,
        selectedSquare.col,
        row,
        col
      );
      if (isValidMove) {
        var move = { from: selectedSquare, to: { row: row, col: col } };
        sendMove(move);
        selectedSquare = null;
        removeValidMoveHighlights();
      }
    }
  }

  function showValidMoves(row, col) {
    var validMoves = getValidMoves(row, col);
    validMoves.forEach(function (move) {
      var squareId = "square" + (move.row * 8 + move.col);
      document.getElementById(squareId).classList.add("valid-move");
    });
  }

  function removeValidMoveHighlights() {
    var squares = document.querySelectorAll(".square");
    squares.forEach(function (square) {
      square.classList.remove("valid-move");
    });
  }

  function sendMove(move) {
    // Implement AJAX request to send move to server
    // Update game state based on server response
    // Update UI with new game state
  }

  function updateGameState(gameState) {
    currentGame = gameState;
    renderBoard();
    document.getElementById("status").textContent =
      "Status: " + gameState.status;
  }

  function renderBoard() {
    var board = currentGame.board;
    for (var i = 0; i < 8; i++) {
      for (var j = 0; j < 8; j++) {
        var piece = board[i][j];
        var squareId = "square" + (i * 8 + j);
        var square = document.getElementById(squareId);
        square.innerHTML = "";
        if (piece !== " ") {
          var pieceElement = document.createElement("div");
          pieceElement.className = "piece";
          pieceElement.textContent = piece;
          pieceElement.classList.add(
            piece === piece.toUpperCase() ? "white-piece" : "black-piece"
          );
          square.appendChild(pieceElement);
        }
      }
    }
  }

  function getValidMoves(row, col) {
    var moves = [];
    // Add move logic here based on piece type
    return moves;
  }

  function isValidMove(fromRow, fromCol, toRow, toCol) {
    // Add move validation logic here
    return true; // For simplicity, consider all moves valid for now
  }

  // Initialize chessboard
  initializeChessboard();

  // Poll the server for updates
  setInterval(function () {
    // Implement AJAX request to get updated game state from server
    // Update UI with new game state
  }, 1000); // Polling interval (ms)
});
