; Auto-generated. Do not edit!


(cl:in-package turtle_battle-msg)


;//! \htmlinclude AttackCommand.msg.html

(cl:defclass <AttackCommand> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass AttackCommand (<AttackCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AttackCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AttackCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtle_battle-msg:<AttackCommand> is deprecated: use turtle_battle-msg:AttackCommand instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AttackCommand>) ostream)
  "Serializes a message object of type '<AttackCommand>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AttackCommand>) istream)
  "Deserializes a message object of type '<AttackCommand>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AttackCommand>)))
  "Returns string type for a message object of type '<AttackCommand>"
  "turtle_battle/AttackCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AttackCommand)))
  "Returns string type for a message object of type 'AttackCommand"
  "turtle_battle/AttackCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AttackCommand>)))
  "Returns md5sum for a message object of type '<AttackCommand>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AttackCommand)))
  "Returns md5sum for a message object of type 'AttackCommand"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AttackCommand>)))
  "Returns full string definition for message of type '<AttackCommand>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AttackCommand)))
  "Returns full string definition for message of type 'AttackCommand"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AttackCommand>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AttackCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'AttackCommand
))
