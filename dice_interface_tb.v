
`timescale 1ns/1ps

module dice_interface_tb;

    reg clk = 0;
    reg reset = 1;
    reg roll = 0;

    wire [2:0] dice_value;
    wire [6:0] seg;

    integer fd;
    integer request_value;
    integer scan_result;

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
        #10;
        reset = 0;

        fd = $fopen("roll_request.txt", "r");

        if (fd == 0) begin
            $display("ERROR: Cannot open roll_request.txt");
            $finish;
        end

        scan_result = $fscanf(fd, "%d", request_value);
        $fclose(fd);

        if (scan_result != 1 ||
            request_value < 1 ||
            request_value > 1000) begin
            $display("ERROR: Invalid roll request");
            $finish;
        end

        // Advance the LFSR before rolling
        repeat (request_value)
            @(negedge clk);

        roll = 1;
        @(posedge clk);
        #1;

        $display("DICE_RESULT=%0d", dice_value);
        $display("SEGMENT_RESULT=%07b", seg);

        roll = 0;
        $finish;
    end

endmodule
