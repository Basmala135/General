; Auto-generated. Do not edit!


(cl:in-package turtle_battle-msg)


;//! \htmlinclude GameState.msg.html

(cl:defclass <GameState> (roslisp-msg-protocol:ros-message)
  ((turtle1_health
    :reader turtle1_health
    :initarg :turtle1_health
    :type cl:integer
    :initform 0)
   (turtle2_health
    :reader turtle2_health
    :initarg :turtle2_health
    :type cl:integer
    :initform 0)
   (turtle1_attacks_remaining
    :reader turtle1_attacks_remaining
    :initarg :turtle1_attacks_remaining
    :type cl:integer
    :initform 0)
   (turtle2_attacks_remaining
    :reader turtle2_attacks_remaining
    :initarg :turtle2_attacks_remaining
    :type cl:integer
    :initform 0))
)

(cl:defclass GameState (<GameState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GameState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GameState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtle_battle-msg:<GameState> is deprecated: use turtle_battle-msg:GameState instead.")))

(cl:ensure-generic-function 'turtle1_health-val :lambda-list '(m))
(cl:defmethod turtle1_health-val ((m <GameState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtle_battle-msg:turtle1_health-val is deprecated.  Use turtle_battle-msg:turtle1_health instead.")
  (turtle1_health m))

(cl:ensure-generic-function 'turtle2_health-val :lambda-list '(m))
(cl:defmethod turtle2_health-val ((m <GameState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtle_battle-msg:turtle2_health-val is deprecated.  Use turtle_battle-msg:turtle2_health instead.")
  (turtle2_health m))

(cl:ensure-generic-function 'turtle1_attacks_remaining-val :lambda-list '(m))
(cl:defmethod turtle1_attacks_remaining-val ((m <GameState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtle_battle-msg:turtle1_attacks_remaining-val is deprecated.  Use turtle_battle-msg:turtle1_attacks_remaining instead.")
  (turtle1_attacks_remaining m))

(cl:ensure-generic-function 'turtle2_attacks_remaining-val :lambda-list '(m))
(cl:defmethod turtle2_attacks_remaining-val ((m <GameState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtle_battle-msg:turtle2_attacks_remaining-val is deprecated.  Use turtle_battle-msg:turtle2_attacks_remaining instead.")
  (turtle2_attacks_remaining m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GameState>) ostream)
  "Serializes a message object of type '<GameState>"
  (cl:let* ((signed (cl:slot-value msg 'turtle1_health)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'turtle2_health)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'turtle1_attacks_remaining)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'turtle2_attacks_remaining)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GameState>) istream)
  "Deserializes a message object of type '<GameState>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'turtle1_health) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'turtle2_health) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'turtle1_attacks_remaining) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'turtle2_attacks_remaining) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GameState>)))
  "Returns string type for a message object of type '<GameState>"
  "turtle_battle/GameState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GameState)))
  "Returns string type for a message object of type 'GameState"
  "turtle_battle/GameState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GameState>)))
  "Returns md5sum for a message object of type '<GameState>"
  "0051aa3ff6623e54a13e3a5509f76a87")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GameState)))
  "Returns md5sum for a message object of type 'GameState"
  "0051aa3ff6623e54a13e3a5509f76a87")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GameState>)))
  "Returns full string definition for message of type '<GameState>"
  (cl:format cl:nil "int32 turtle1_health~%int32 turtle2_health~%int32 turtle1_attacks_remaining~%int32 turtle2_attacks_remaining~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GameState)))
  "Returns full string definition for message of type 'GameState"
  (cl:format cl:nil "int32 turtle1_health~%int32 turtle2_health~%int32 turtle1_attacks_remaining~%int32 turtle2_attacks_remaining~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GameState>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GameState>))
  "Converts a ROS message object to a list"
  (cl:list 'GameState
    (cl:cons ':turtle1_health (turtle1_health msg))
    (cl:cons ':turtle2_health (turtle2_health msg))
    (cl:cons ':turtle1_attacks_remaining (turtle1_attacks_remaining msg))
    (cl:cons ':turtle2_attacks_remaining (turtle2_attacks_remaining msg))
))
