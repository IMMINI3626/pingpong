from PingPonglib.protocols.generateprotocol import GenerateProtocol
from PingPonglib.operations.stepper.stepperoperation import StepperOperation
from PingPonglib.operations.servo.servooperation import ServoOperation
from PingPonglib.operations.ledmatrix.ledmatrixoperation import LEDMatrixOperation
from PingPonglib.operations.cube.cubeoperation import CubeOperation
from PingPonglib.operations.music.musicoperation import MusicOperation

class OperationDerived(StepperOperation, ServoOperation, LEDMatrixOperation, CubeOperation, MusicOperation):
    def __init__(self, number, group_id, robot_status, start_check, write):
        self._GenerateProtocolInstance = GenerateProtocol(number, group_id)
        self._robot_status = robot_status
        self._start_check_copy = start_check
        self._write_copy = write
        StepperOperation.__init__(self, number, group_id, robot_status, start_check, write)
        ServoOperation.__init__(self, number, group_id, robot_status, start_check, write)
        LEDMatrixOperation.__init__(self, number, group_id, robot_status, start_check, write)
        CubeOperation.__init__(self, number, group_id, robot_status, start_check, write)
        MusicOperation.__init__(self, number, group_id, robot_status, start_check, write)