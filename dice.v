`timescale 1ns/1ps
module digital_dice (
    input wire clk,
    input wire reset,
    input wire roll,
    output reg [2:0] dice_value
);

    reg [7:0] lfsr;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            lfsr       <= 8'b10110101;
            dice_value <= 3'd1;
        end
        else begin
            lfsr <= {
                lfsr[6:0],
                lfsr[7] ^ lfsr[5] ^
                lfsr[4] ^ lfsr[3]
            };

            if (roll) begin
                case (lfsr[2:0])
                    3'd0: dice_value <= 3'd1;
                    3'd1: dice_value <= 3'd2;
                    3'd2: dice_value <= 3'd3;
                    3'd3: dice_value <= 3'd4;
                    3'd4: dice_value <= 3'd5;
                    3'd5: dice_value <= 3'd6;
                    3'd6: dice_value <= 3'd1;
                    3'd7: dice_value <= 3'd2;
                    default: dice_value <= 3'd1;
                endcase
            end
        end
    end

endmodule
