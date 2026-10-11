`timescale 1ns/1ps
module seg7_decoder (
    input wire [2:0] dice_value,
    output reg [6:0] seg
);

    // Active-low output
    // Segment order: a, b, c, d, e, f, g

    always @(*) begin
        case (dice_value)
            3'd1: seg = 7'b1111001;
            3'd2: seg = 7'b0100100;
            3'd3: seg = 7'b0110000;
            3'd4: seg = 7'b0011001;
            3'd5: seg = 7'b0010010;
            3'd6: seg = 7'b0000010;

            default: seg = 7'b1111111;
        endcase
    end

endmodule
