pragma solidity ^0.8.13;

import "./MintChocolate.sol";

contract Setup {
    MintChocolate public immutable TARGET;
    constructor() payable {
        TARGET = new MintChocolate();

    }

    function isSolved() public view returns (bool) {
        return TARGET.goldenTicket();
    }
}