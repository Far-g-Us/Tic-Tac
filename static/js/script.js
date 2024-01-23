let board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
];

let currentPlayer = 'X'; // X will always start first

function init() {
    let gameBoard = document.getElementById('game-board');

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            let cell = document.createElement('div');
            cell.className = 'cell';
            cell.addEventListener('click', cellClicked);
            cell.dataset.row = i;
            cell.dataset.col = j;
            gameBoard.appendChild(cell);
        }
    }
}

function cellClicked(event) {
    let row = event.target.dataset.row;
    let col = event.target.dataset.col;

    if (board[row][col] === '') {
        board[row][col] = currentPlayer;
        event.target.textContent = currentPlayer;
        if (checkWinner(row, col)) {
            alert(`${currentPlayer} wins!`);
            return;
        }
        currentPlayer = (currentPlayer === 'X') ? 'O' : 'X';
    }
}

function checkWinner(row, col) {
    // Check row
    if (board[row][0] === currentPlayer && board[row][1] === currentPlayer && board[row][2] === currentPlayer) {
        return true;
    }
    // Check column
    if (board[0][col] === currentPlayer && board[1][col] === currentPlayer && board[2][col] === currentPlayer) {
        return true;
    }
    // Check diagonals
    if (row === col && board[0][0] === currentPlayer && board[1][1] === currentPlayer && board[2][2] === currentPlayer) {
        return true;
    }
    if (Number(row) + Number(col) === 2 && board[0][2] === currentPlayer && board[1][1] === currentPlayer && board[2][0] === currentPlayer) {
        return true;
    }
    return false;
}

window.onload = init;