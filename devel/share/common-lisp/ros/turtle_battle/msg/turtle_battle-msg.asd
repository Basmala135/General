
(cl:in-package :asdf)

(defsystem "turtle_battle-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AttackCommand" :depends-on ("_package_AttackCommand"))
    (:file "_package_AttackCommand" :depends-on ("_package"))
    (:file "GameState" :depends-on ("_package_GameState"))
    (:file "_package_GameState" :depends-on ("_package"))
  ))