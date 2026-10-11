
`timescale 1ns/1ps

module dice_tb;

    reg clk;
    reg reset;
    reg roll;

    wire [2:0] dice_value;
    wire [6:0] seg;

    digital_dice uut (
        .clk(clk),
        .reset(reset),
        .roll(roll),
        .dice_value(dice_value)
    );

    seg7_decoder display_unit (
        .dice_value(dice_value),
        .seg(seg)
    );

    always #5 clk = ~clk;

    initial begin
        $dumpfile("dice.vcd");
        $dumpvars(0, dice_tb);

        clk = 0;
        reset = 1;
        roll = 0;

        #10;
        reset = 0;

        repeat (12) begin
            #2 roll = 1;
            #10;

            $display(
                "Time=%0t | Dice=%0d | Segments=%b",
                $time, dice_value, seg
            );

            roll = 0;
            #10;
        end

        $finish;
    end

endmodule
